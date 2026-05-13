# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_07:26:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 07:26:21 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.038 |  |
| 2026-05-13 07:20:22 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-13 07:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.63 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-13 07:11:29 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-13 07:09:59 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-05-13 07:09:43 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.046 |  |
| 2026-05-13 07:09:27 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-13 07:08:25 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 07:07:55 | Galgamuwa (Mee Oya) | 2.08 | 🟢 Normal | -0.035 |  |
| 2026-05-13 07:07:12 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:07:10 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-13 07:07:09 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-13 07:06:06 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.064 |  |
| 2026-05-13 07:06:02 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-05-13 07:05:52 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:05:50 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-13 07:05:47 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-05-13 07:05:43 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-13 07:05:14 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:04:01 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.093 |  |
| 2026-05-13 07:03:48 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-13 07:03:15 | Katharagama (Menik Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-05-13 07:03:08 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 07:02:16 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 07:02:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-13 07:02:04 | Thanthirimale (Malwathu Oya) | 3.46 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-13 07:01:51 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-05-13 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-13 07:01:37 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-13 07:01:34 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 07:01:23 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:01:19 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.060 |  |
| 2026-05-13 07:01:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-13 07:01:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-13 07:01:11 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.046 |  |
| 2026-05-13 07:00:52 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 07:00:09 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 07:01:37 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-13 06:01:22 | Moragaswewa (Deduru Oya) | 1.82 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 07:07:09 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-13 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-13 07:09:59 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-05-13 07:01:51 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-05-13 07:11:29 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-13 07:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-13 07:05:43 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-13 07:00:52 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 07:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.63 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-13 07:05:50 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-13 07:02:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-13 07:01:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-13 07:02:16 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-13 07:20:22 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-13 07:08:25 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 07:01:34 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 07:03:08 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 07:02:04 | Thanthirimale (Malwathu Oya) | 3.46 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-13 07:03:48 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:05:14 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:05:52 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:07:12 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:01:23 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-13 07:09:27 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-13 07:07:10 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-13 07:00:09 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.014 |  |
| 2026-05-13 07:06:02 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-05-13 07:05:47 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-05-13 06:02:11 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.024 |  |
| 2026-05-13 07:03:15 | Katharagama (Menik Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-05-13 07:07:55 | Galgamuwa (Mee Oya) | 2.08 | 🟢 Normal | -0.035 |  |
| 2026-05-13 07:26:21 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.038 |  |
| 2026-05-13 07:01:11 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.046 |  |
| 2026-05-13 07:09:43 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.046 |  |
| 2026-05-13 07:01:19 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.060 |  |
| 2026-05-13 07:06:06 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.064 |  |
| 2026-05-13 07:04:01 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)