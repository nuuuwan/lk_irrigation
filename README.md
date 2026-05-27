# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_09:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 09:08:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-05-27 09:07:41 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.049 |  |
| 2026-05-27 09:07:24 | Magura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-05-27 09:06:11 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.019 |  |
| 2026-05-27 09:05:44 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:05:22 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:05:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:05:11 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-05-27 09:05:02 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:05:01 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:04:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-27 09:04:34 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.031 |  |
| 2026-05-27 09:04:32 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:04:29 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-05-27 09:04:22 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:04:01 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 09:03:56 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 09:03:44 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:03:34 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:03:32 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.042 |  |
| 2026-05-27 09:03:25 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:03:09 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.064 |  |
| 2026-05-27 09:02:49 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-27 09:02:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:02:20 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:02:09 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 09:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-27 09:01:44 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:40 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 09:01:26 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.021 |  |
| 2026-05-27 09:00:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:31 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:19 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 08:23:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 09:02:49 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-27 09:04:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-27 09:02:09 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 09:03:56 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 09:01:40 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 09:02:20 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:05:22 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:05:01 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:03:34 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 09:00:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:44 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:04:22 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:08:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:04:32 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 08:11:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:05:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:02:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:01:26 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:31 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 09:00:19 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 08:17:46 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-05-27 09:03:25 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:05:44 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:04:01 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:05:02 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-27 09:07:24 | Magura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-05-27 09:06:11 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.019 |  |
| 2026-05-27 09:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-05-27 09:04:29 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-05-27 09:01:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.021 |  |
| 2026-05-27 09:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.023 |  |
| 2026-05-27 09:05:11 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-05-27 09:04:34 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.031 |  |
| 2026-05-27 09:03:32 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.042 |  |
| 2026-05-27 09:07:41 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.049 |  |
| 2026-05-27 09:03:09 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)