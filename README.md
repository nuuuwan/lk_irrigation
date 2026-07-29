# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_20:28:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 20:28:03 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:25:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:19:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.008 |  |
| 2026-07-29 20:16:30 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-07-29 20:12:01 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:10:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:10:17 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.029 |  |
| 2026-07-29 20:09:57 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:06:17 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:05:34 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2026-07-29 20:05:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:55 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:42 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.546 | 🔺 Rising |
| 2026-07-29 20:03:37 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:22 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-29 20:03:11 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:11 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 20:02:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -144.000 |  |
| 2026-07-29 20:02:56 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -144.000 |  |
| 2026-07-29 20:02:49 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-29 20:02:42 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-07-29 20:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-07-29 20:02:20 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:02:09 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:51 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-29 20:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-07-29 20:01:19 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:12 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 20:00:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:41 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 20:03:42 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.546 | 🔺 Rising |
| 2026-07-29 20:02:49 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-29 20:01:12 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 20:03:11 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 20:01:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:10:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:25:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:02:09 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:19 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 19:05:38 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:06:17 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:28:03 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:55 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:16:30 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:11 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:12:01 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:05:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:37 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:00:41 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:01:51 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:02:20 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-29 20:03:22 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-29 20:19:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.008 |  |
| 2026-07-29 20:05:34 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.010 |  |
| 2026-07-29 20:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-29 20:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-07-29 20:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-07-29 20:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-07-29 20:10:17 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.029 |  |
| 2026-07-29 20:01:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-29 20:02:42 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-07-29 20:02:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)