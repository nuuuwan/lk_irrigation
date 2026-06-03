# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_03:02:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,832 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 03:02:35 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-04 03:02:31 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:14 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 03:01:12 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 03:00:24 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:40:13 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-04 02:39:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:18:24 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-04 02:13:17 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 02:13:15 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 02:12:43 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 02:13:17 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 02:06:14 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-06-04 02:01:29 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-06-04 02:40:13 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-04 03:02:35 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-04 02:04:42 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-04 02:06:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-04 02:04:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-04 02:05:52 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-04 02:03:46 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-04 02:18:24 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-04 02:01:04 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 02:05:27 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 02:03:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 02:03:49 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 02:05:02 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-04 03:01:14 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 02:04:16 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:00:24 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:31 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:03:20 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:03:45 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:01:14 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:12 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:05:10 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:39:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:04:38 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 02:12:43 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-06-04 02:06:01 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 02:03:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)