# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_08:16:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,330 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 08:16:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:15:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:11:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:10:03 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:09:50 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:07:24 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:06:52 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:06:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-01-03 08:06:27 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-03 08:05:54 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:05:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:05:37 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-03 08:05:25 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:05:24 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.019 |  |
| 2026-01-03 08:05:18 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:05:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-01-03 08:05:05 | Galgamuwa (Mee Oya) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 08:05:05 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.028 |  |
| 2026-01-03 08:04:31 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:03:50 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:03:50 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 08:03:49 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:03:36 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:03:32 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:03:00 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:02:44 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:32 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:24 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.200 |  |
| 2026-01-03 08:02:21 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-01-03 08:02:10 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-01-03 08:01:50 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:16 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:01:15 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:00:51 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 08:05:37 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-03 08:06:27 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-03 08:05:05 | Galgamuwa (Mee Oya) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 08:03:50 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 08:01:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:04:31 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:05:18 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:15:17 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:10:03 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:44 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:07:24 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:21 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:09:50 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:15 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:03:50 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:05:25 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:11:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:02:32 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:16:08 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:05:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:03:32 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-01-03 08:01:50 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:05:54 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:03:00 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:05:24 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.019 |  |
| 2026-01-03 08:00:51 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:03:49 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:03:36 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:01:16 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:05:05 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.028 |  |
| 2026-01-03 08:05:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-01-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-01-03 08:02:10 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-01-03 08:06:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-01-03 08:02:24 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)