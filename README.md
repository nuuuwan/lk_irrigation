# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_11:11:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 11:11:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:08:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:08:06 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.028 |  |
| 2026-07-30 11:06:43 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:11 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-07-30 11:05:23 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:04:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:04:17 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-30 11:04:16 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:04:12 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.030 |  |
| 2026-07-30 11:04:02 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-07-30 11:03:57 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-30 11:03:53 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:03:37 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-07-30 11:03:32 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 11:03:19 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:03:04 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 11:02:59 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.053 |  |
| 2026-07-30 11:02:40 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:27 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-07-30 11:02:19 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-07-30 11:02:14 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:13 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-30 11:02:13 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:09 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:06 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-07-30 11:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:01:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:01:51 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-07-30 11:01:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-07-30 11:00:52 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-30 11:00:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:00:22 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 11:03:37 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-07-30 11:01:51 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-07-30 11:00:22 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-30 11:02:13 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-30 11:03:57 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-30 11:02:19 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 11:03:04 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 11:03:32 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 11:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:00:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:05:23 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:01:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:09 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:04:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:13 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:04:16 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:03:19 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:03:53 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:11:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:08:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:14 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:43 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:02:40 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:16 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 11:06:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-30 10:02:05 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-30 11:04:17 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-30 11:00:52 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-30 10:07:20 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-07-30 11:02:27 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-07-30 11:01:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-07-30 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-07-30 11:02:06 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-07-30 11:08:06 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.028 |  |
| 2026-07-30 11:06:11 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-07-30 11:04:12 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.030 |  |
| 2026-07-30 11:04:02 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-07-30 11:02:59 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)