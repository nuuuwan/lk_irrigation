# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_15:10:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 15:10:37 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.053 |  |
| 2026-07-24 15:09:23 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:08:53 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:08:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-07-24 15:07:09 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:56 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:09 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:54 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:03 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:03:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-24 15:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-24 15:03:26 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-24 15:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:03:22 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:03:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.045 |  |
| 2026-07-24 15:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:03:10 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:28 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:02:22 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:02:19 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-24 15:02:18 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:03 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:42 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:30 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-07-24 15:01:22 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.033 |  |
| 2026-07-24 15:01:18 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-24 15:00:40 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:20 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 15:02:19 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-24 15:03:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-24 15:00:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-24 15:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-07-24 15:04:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:08:53 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:40 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:17 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:07:09 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:18 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:54 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:09:23 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:22 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:42 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:56 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:05:09 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:03 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:04:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:02:03 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:03:10 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:03:22 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:01:18 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:00:20 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 15:08:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-07-24 15:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:02:28 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:02:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-24 15:01:30 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-07-24 15:03:26 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-24 15:01:22 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.033 |  |
| 2026-07-24 15:03:22 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.045 |  |
| 2026-07-24 15:10:37 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)