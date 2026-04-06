# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_09:35:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 09:35:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-06 09:23:16 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:14:57 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:11:56 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:09:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 09:09:06 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.048 |  |
| 2026-04-06 09:07:51 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:07:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:07:23 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:48 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.068 |  |
| 2026-04-06 09:06:31 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:29 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:14 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:05 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:05:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:05:17 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.201 |  |
| 2026-04-06 09:05:08 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:04:19 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:04:17 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:04:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:04:10 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.118 |  |
| 2026-04-06 09:03:19 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 09:03:13 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:02:42 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-06 09:02:27 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:02:11 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 09:02:09 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.043 |  |
| 2026-04-06 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.170 |  |
| 2026-04-06 09:02:07 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.104 |  |
| 2026-04-06 09:01:52 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-06 09:01:30 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:01:23 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 09:01:20 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.096 |  |
| 2026-04-06 09:01:05 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:00:49 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.100 |  |
| 2026-04-06 09:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:00:33 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:00:32 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:00:09 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 09:03:19 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 09:35:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-06 09:02:11 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 09:09:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-06 09:01:23 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 09:00:32 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:14 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:07:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:02:27 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:23:16 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:04:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:07:51 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:11:56 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:01:52 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:05:08 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:04:19 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:31 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:14:57 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:06:29 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 09:05:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:01:05 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:06:05 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-06 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-06 09:00:09 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-04-06 09:03:13 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:04:17 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:01:30 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:00:33 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-06 09:02:09 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.043 |  |
| 2026-04-06 09:09:06 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.048 |  |
| 2026-04-06 09:06:48 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.068 |  |
| 2026-04-06 09:01:20 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.096 |  |
| 2026-04-06 09:00:49 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.100 |  |
| 2026-04-06 09:02:07 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.104 |  |
| 2026-04-06 09:04:10 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.118 |  |
| 2026-04-06 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.170 |  |
| 2026-04-06 09:05:17 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)