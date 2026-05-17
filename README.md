# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_03:02:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 03:02:15 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-05-18 03:02:10 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:02:08 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:01:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:01:58 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-05-18 03:01:33 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 03:01:27 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.071 |  |
| 2026-05-18 03:01:15 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-18 03:01:10 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-05-18 03:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:00:52 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:48:47 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:38:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.006 |  |
| 2026-05-18 02:32:11 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:15:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:15:47 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:15:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.26 | 🟡 Alert | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 02:15:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.26 | 🟡 Alert | -0.042 |  |
| 2026-05-18 01:44:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-18 03:01:15 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-18 02:04:43 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-18 01:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 02:00:17 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:05:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:01:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:02:08 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:01:47 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:00:52 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:02:10 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:15:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:48:47 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:02:24 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:02:52 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:05:46 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-18 02:38:10 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.006 |  |
| 2026-05-18 01:46:59 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.008 |  |
| 2026-05-18 03:01:33 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 02:01:21 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-18 03:01:58 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-05-18 03:01:10 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-05-18 02:07:12 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-18 02:05:25 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-05-18 01:06:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-18 03:02:15 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-05-18 02:01:16 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-05-18 02:02:37 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-18 01:05:33 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.060 |  |
| 2026-05-18 03:01:27 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.071 |  |
| 2026-05-18 02:05:14 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.105 |  |
| 2026-05-18 02:01:43 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.262 |  |
| 2026-05-18 02:01:59 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -1.029 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)