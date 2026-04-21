# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_07:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 07:17:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:11:08 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-04-21 07:11:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-21 07:10:33 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-21 07:08:49 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 07:07:15 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:06:52 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-21 07:06:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.180 |  |
| 2026-04-21 07:06:06 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:05:48 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-04-21 07:05:26 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.237 |  |
| 2026-04-21 07:05:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-04-21 07:05:01 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-04-21 07:04:56 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-04-21 07:04:56 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.139 |  |
| 2026-04-21 07:04:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-21 07:04:17 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 07:04:01 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-21 07:03:32 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-04-21 07:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-04-21 07:03:11 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-04-21 07:03:08 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:02:58 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 07:02:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-04-21 07:02:13 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2026-04-21 07:02:09 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | -0.287 |  |
| 2026-04-21 07:02:08 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:02:01 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-21 07:01:56 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:01:16 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 07:01:12 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:01:10 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 07:01:03 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-04-21 07:00:57 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:00:37 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.112 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 07:03:11 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-04-21 07:05:01 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-04-21 07:02:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-04-21 07:06:52 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-04-21 07:02:01 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-21 07:04:01 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-21 07:10:33 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-21 07:04:17 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 07:01:10 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 07:08:49 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 07:06:06 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:02:08 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:07:15 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 07:02:58 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 07:01:16 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 07:11:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-21 07:01:12 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:02:13 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:00:57 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:01:56 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:03:08 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:17:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-21 07:04:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-21 07:04:56 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-04-21 07:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-04-21 06:14:20 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.026 |  |
| 2026-04-21 07:11:08 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-04-21 07:03:32 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-04-21 07:01:03 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-04-21 07:05:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-04-21 06:00:33 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.085 |  |
| 2026-04-21 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2026-04-21 07:05:48 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-04-21 07:00:37 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.112 |  |
| 2026-04-21 07:04:56 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.139 |  |
| 2026-04-21 07:06:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.180 |  |
| 2026-04-21 07:05:26 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.237 |  |
| 2026-04-21 07:02:09 | Thanamalwila (Kirindi Oya) | 2.65 | 🟢 Normal | -0.287 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)