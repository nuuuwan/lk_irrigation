# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_02:27:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **209,171 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 02:27:29 | Moraketiya (Walawe Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:11:39 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-18 02:09:55 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:07:24 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-07-18 02:06:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:04:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:04:28 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:04:12 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-18 02:03:53 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:03:35 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:03:30 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:03:08 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:02:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-18 02:02:45 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-18 02:02:41 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-18 02:02:34 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-18 02:02:12 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:35 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-18 02:01:20 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.103 |  |
| 2026-07-18 02:01:20 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:03 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:00:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 02:07:24 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-07-18 02:02:15 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-18 01:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-18 02:11:39 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-18 02:02:41 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-18 02:02:45 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-18 01:03:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-18 02:01:35 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-18 02:03:08 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:04:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:03:30 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 02:01:20 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:03 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:12 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:03:53 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:06:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 23:03:17 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-18 01:06:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:04:28 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 01:01:57 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 00:00:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:27:29 | Moraketiya (Walawe Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-18 01:16:26 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-18 01:02:05 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:09:55 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:03:48 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:06:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:03:35 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:04:12 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-18 02:02:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-18 02:00:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-18 01:01:30 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.011 |  |
| 2026-07-18 01:07:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.011 |  |
| 2026-07-17 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-18 02:01:20 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)