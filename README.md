# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_09:10:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 09:10:22 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | -0.020 |  |
| 2026-05-29 09:06:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-29 09:06:20 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:06:08 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.093 |  |
| 2026-05-29 09:06:03 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.053 |  |
| 2026-05-29 09:06:03 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.089 |  |
| 2026-05-29 09:05:39 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 09:05:38 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:04:56 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:04:51 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:04:40 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:04:29 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.116 |  |
| 2026-05-29 09:04:14 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.035 |  |
| 2026-05-29 09:03:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:03:37 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 09:03:36 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:03:35 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-05-29 09:03:17 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-05-29 09:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:52 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-05-29 09:02:46 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:40 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:29 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:25 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-29 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 09:02:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-29 09:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-29 09:01:57 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-29 09:01:55 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:31 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:25 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:01:22 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:00:45 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 09:00:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:00:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.020 |  |
| 2026-05-29 08:59:01 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-29 08:20:32 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 09:10:22 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | -0.020 |  |
| 2026-05-29 09:06:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-29 09:01:57 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-29 08:01:07 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-29 08:59:01 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-29 09:02:25 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-29 09:00:45 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 09:02:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-29 09:03:37 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 09:05:39 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 09:02:46 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:55 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:22 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:05:38 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:01:31 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:29 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:03:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:06:20 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:04:56 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:03:36 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 09:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-29 09:02:52 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-05-29 09:03:35 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-05-29 09:04:51 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:04:40 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:00:16 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:02:40 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:00:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:01:25 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-29 09:04:14 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.035 |  |
| 2026-05-29 09:06:03 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.053 |  |
| 2026-05-29 09:03:17 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.079 |  |
| 2026-05-29 09:06:03 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.089 |  |
| 2026-05-29 09:06:08 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.093 |  |
| 2026-05-29 09:04:29 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)