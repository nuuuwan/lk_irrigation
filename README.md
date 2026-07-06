# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_01:37:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,292 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 01:37:37 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.007 |  |
| 2026-07-07 01:27:33 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-07-07 01:21:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-07-07 01:19:10 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:19:09 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:19:07 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:18:04 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.008 |  |
| 2026-07-07 01:15:19 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-07-07 01:12:11 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:10:41 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-07 01:10:32 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:10:02 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:09:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:08:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:07:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:05:47 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-07 01:05:27 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:05:21 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:04:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-07 01:04:29 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:03:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.318 |  |
| 2026-07-07 01:02:59 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:57 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 01:21:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-07-07 01:10:41 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-07 01:04:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-07 01:01:52 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:00:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:01:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:04:29 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:01:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:19:10 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 00:45:19 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:59 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:01:29 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:12:11 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:22 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:07:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:01:31 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:00:01 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-07 00:02:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:08:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:01:40 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:09:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:31 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-07-07 01:37:37 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.007 |  |
| 2026-07-07 01:18:04 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.008 |  |
| 2026-07-07 01:10:32 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:10:02 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:05:21 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:05:47 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:00:53 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-07 01:15:19 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-07-07 01:27:33 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.022 |  |
| 2026-07-06 22:14:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-07-07 00:11:11 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.055 |  |
| 2026-07-07 01:03:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.318 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)