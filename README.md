# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_13:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,192 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 13:18:08 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-20 13:17:09 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:16:39 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-04-20 13:14:16 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.097 |  |
| 2026-04-20 13:12:27 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-20 13:09:21 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-04-20 13:08:42 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 13:06:33 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:05:25 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 13:04:36 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:04:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:04:25 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-20 13:04:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:03:45 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:03:35 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:03:28 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:03:21 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-20 13:03:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-20 13:03:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-20 13:02:33 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:33 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:02:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:02:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.050 |  |
| 2026-04-20 13:01:58 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:01:51 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:01:48 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.130 |  |
| 2026-04-20 13:01:38 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-04-20 13:01:33 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-04-20 13:00:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-20 13:00:52 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 13:01:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-04-20 13:03:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-20 13:00:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-20 13:12:27 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-20 13:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-20 13:05:25 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 13:08:42 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 13:02:33 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:33 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:04:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:03:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:03:35 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:00:52 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:01:51 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:02:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:06:33 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:01:33 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:04:25 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:03:28 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:17:09 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:16:39 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-04-20 13:18:08 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-20 13:03:45 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:04:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:02:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:02:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:01:58 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:04:36 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-04-20 13:02:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-20 13:09:21 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-04-20 13:03:21 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-20 13:01:38 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-04-20 12:02:22 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2026-04-20 13:02:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.050 |  |
| 2026-04-20 13:14:16 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.097 |  |
| 2026-04-20 13:01:48 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)