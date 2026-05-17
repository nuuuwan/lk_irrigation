# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_06:33:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,041 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 06:33:18 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | -0.083 |  |
| 2026-05-17 06:12:15 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:10:09 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:08:31 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.144 |  |
| 2026-05-17 06:08:15 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.048 |  |
| 2026-05-17 06:07:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:05:28 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 06:05:25 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:05:11 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:05:05 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:04:42 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:04:31 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:04:07 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.019 |  |
| 2026-05-17 06:04:05 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:03:58 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.182 |  |
| 2026-05-17 06:03:19 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | -0.043 |  |
| 2026-05-17 06:03:06 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 06:03:06 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:03:01 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-17 06:02:42 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:02:37 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | -0.017 |  |
| 2026-05-17 06:02:23 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:02:21 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-17 06:02:16 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:02:15 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.124 |  |
| 2026-05-17 06:01:19 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.003 |  |
| 2026-05-17 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:01:15 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:01:01 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:01:01 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.066 |  |
| 2026-05-17 06:00:59 | Moragaswewa (Deduru Oya) | 1.61 | 🟢 Normal | -1.241 |  |
| 2026-05-17 06:00:45 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-05-17 06:00:23 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-17 06:00:10 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 05:57:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.88 | 🟠 Minor Flood | -0.182 |  |
| 2026-05-17 05:53:44 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -1.241 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 06:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.86 | 🟠 Minor Flood | -0.182 |  |
| 2026-05-17 06:02:21 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-17 06:00:23 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-17 06:05:28 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 06:03:06 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 06:00:10 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 06:01:19 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.003 |  |
| 2026-05-17 06:05:05 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:01:15 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:04:42 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:10:09 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:12:15 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:04:05 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:02:42 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:03:58 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:05:11 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:05:25 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:01:01 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:09 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:02:15 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 06:03:06 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:02:16 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:02:23 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:04:31 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:07:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-17 06:02:37 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | -0.017 |  |
| 2026-05-17 06:04:07 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.019 |  |
| 2026-05-17 06:03:01 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-17 06:00:45 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 06:03:19 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | -0.043 |  |
| 2026-05-17 06:08:15 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.048 |  |
| 2026-05-17 06:01:01 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.066 |  |
| 2026-05-17 06:33:18 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | -0.083 |  |
| 2026-05-17 06:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.124 |  |
| 2026-05-17 06:08:31 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.144 |  |
| 2026-05-17 06:00:59 | Moragaswewa (Deduru Oya) | 1.61 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)