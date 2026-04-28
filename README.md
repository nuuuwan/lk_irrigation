# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_08:15:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 08:15:28 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:15:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-04-28 08:14:56 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-28 08:11:49 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:10:06 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.097 |  |
| 2026-04-28 08:09:58 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 08:09:00 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:08:59 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-04-28 08:08:09 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.018 |  |
| 2026-04-28 08:06:23 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-28 08:06:00 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-28 08:05:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:05:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:05:28 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.029 |  |
| 2026-04-28 08:05:26 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-04-28 08:04:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:04:25 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:04:17 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:04:03 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:03:56 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.196 |  |
| 2026-04-28 08:03:43 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:03:29 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2026-04-28 08:03:24 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:03:18 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 08:03:12 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.057 |  |
| 2026-04-28 08:02:55 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:02:55 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.074 |  |
| 2026-04-28 08:02:19 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.075 |  |
| 2026-04-28 08:02:18 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.061 |  |
| 2026-04-28 08:02:13 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-28 08:02:11 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:02:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:02:09 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:02:00 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:01:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:01:22 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 08:14:56 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-28 08:06:00 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-28 08:06:23 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-28 08:03:18 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 08:02:13 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-28 08:02:55 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 08:09:58 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 08:02:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:01:22 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:02:00 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 08:03:43 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:04:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:11:49 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:05:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:02:55 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:05:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-28 07:18:31 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:01:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:09:00 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:15:28 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:02:11 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 08:04:25 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:02:09 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:04:17 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:03:24 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:04:03 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-28 08:08:09 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.018 |  |
| 2026-04-28 08:08:59 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-04-28 08:05:26 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-04-28 08:03:29 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2026-04-28 08:15:22 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-04-28 08:05:28 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.029 |  |
| 2026-04-28 08:03:12 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.057 |  |
| 2026-04-28 08:02:18 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.061 |  |
| 2026-04-28 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.074 |  |
| 2026-04-28 08:02:19 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.075 |  |
| 2026-04-28 08:10:06 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.097 |  |
| 2026-04-28 08:03:56 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)