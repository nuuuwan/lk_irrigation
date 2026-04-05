# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_09:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 09:13:16 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.084 |  |
| 2026-04-05 09:11:20 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:09:40 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:08:46 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.037 |  |
| 2026-04-05 09:08:11 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 09:07:04 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-05 09:06:44 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:06:30 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.104 |  |
| 2026-04-05 09:05:32 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-05 09:05:01 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-05 09:04:29 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.061 |  |
| 2026-04-05 09:04:19 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:04:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:04:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 09:03:49 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:03:38 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.086 |  |
| 2026-04-05 09:03:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:03:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-04-05 09:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:58 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:52 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 09:02:51 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:20 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-04-05 09:02:17 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:04 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:04 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.140 |  |
| 2026-04-05 09:01:56 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:46 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:01:21 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:17 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:01:15 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-05 09:00:49 | Thanthirimale (Malwathu Oya) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:00:36 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 09:05:01 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-05 09:02:52 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 09:01:15 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-05 09:04:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:01:17 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:00:49 | Thanthirimale (Malwathu Oya) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:04:19 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 09:02:04 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:46 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:21 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:17 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:48 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:58 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:03:49 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:03:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:06:44 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:02:51 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:11:20 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:56 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:08:11 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-05 09:07:04 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-05 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-04-05 08:04:19 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:04:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:01:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:09:40 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-05 09:05:32 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-05 09:00:36 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.022 |  |
| 2026-04-05 08:03:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.023 |  |
| 2026-04-05 09:03:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-04-05 09:08:46 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.037 |  |
| 2026-04-05 09:02:20 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-04-05 09:04:29 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.061 |  |
| 2026-04-05 09:13:16 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.084 |  |
| 2026-04-05 09:03:38 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.086 |  |
| 2026-04-05 09:06:30 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.104 |  |
| 2026-04-05 09:02:04 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)