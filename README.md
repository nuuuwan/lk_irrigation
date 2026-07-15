# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_21:12:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 21:12:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-07-15 21:10:06 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:10:04 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 21:07:53 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:07:50 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | -0.066 |  |
| 2026-07-15 21:07:26 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:06:29 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:06:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:05:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:05:06 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:49 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.088 |  |
| 2026-07-15 21:04:39 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:14 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-07-15 21:04:06 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:04 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:58 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:06 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-15 21:03:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:49 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:43 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:39 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-07-15 21:02:35 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:30 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-15 21:02:19 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:16 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-15 21:01:39 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:35 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.100 |  |
| 2026-07-15 21:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:17 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:10 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:00:28 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 21:02:39 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-07-15 21:00:28 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 21:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 21:04:04 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:43 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:05:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:35 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:06:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:02:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:49 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:06 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:10:04 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:58 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:07:26 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:39 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:07:53 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:35 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:00 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:02:19 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:17 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:03:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:06:29 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:10 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:04:16 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:10:06 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:01:39 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:05:06 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:14:35 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-07-15 21:02:16 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-15 21:03:06 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-15 21:04:14 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-07-15 21:02:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-15 21:12:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-07-15 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.062 |  |
| 2026-07-15 21:07:50 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | -0.066 |  |
| 2026-07-15 21:04:49 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.088 |  |
| 2026-07-15 21:01:24 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)