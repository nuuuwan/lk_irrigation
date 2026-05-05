# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_06:25:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 06:25:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-05-05 06:18:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-05 06:14:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 06:14:37 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.006 |  |
| 2026-05-05 06:14:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.128 |  |
| 2026-05-05 06:13:27 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:09:18 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-05 06:06:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:06:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:06:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:05:51 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:48 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-05 06:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:04:56 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-05-05 06:04:51 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:04:47 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-05 06:04:37 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.089 |  |
| 2026-05-05 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.133 |  |
| 2026-05-05 06:04:00 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.053 |  |
| 2026-05-05 06:03:27 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.123 |  |
| 2026-05-05 06:02:59 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:02:40 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-05-05 06:02:39 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:02:33 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:01:58 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:01:44 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 06:01:39 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:01:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:01:20 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:00:45 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-05-05 06:00:42 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.146 |  |
| 2026-05-05 06:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 06:00:36 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 06:09:18 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-05 06:04:47 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-05 06:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 06:05:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-05 06:01:44 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 06:14:41 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 06:18:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-05 06:04:51 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:01:58 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:02:59 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:02:33 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:04:00 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:02:39 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:06:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:06:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:51 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:48 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:05:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:13:27 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:01:20 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:25:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-05-05 06:14:37 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.006 |  |
| 2026-05-05 06:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:01:39 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:01:30 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:06:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-05 06:00:36 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-05-05 06:04:56 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-05-05 06:00:45 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-05-05 06:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.053 |  |
| 2026-05-05 05:05:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-05-05 06:04:37 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.089 |  |
| 2026-05-05 06:02:40 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-05-05 06:03:27 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.123 |  |
| 2026-05-05 06:14:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.128 |  |
| 2026-05-05 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.133 |  |
| 2026-05-05 06:00:42 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)