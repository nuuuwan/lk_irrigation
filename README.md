# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_10:19:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 10:19:30 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 10:11:08 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-07 10:10:57 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 10:10:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-07 10:09:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:07:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:07:23 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-07 10:07:01 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-07 10:06:44 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-06-07 10:06:36 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 10:06:23 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-07 10:05:52 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:05:35 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-07 10:05:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-06-07 10:05:27 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-07 10:05:16 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2026-06-07 10:05:05 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 10:04:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:04:18 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-07 10:04:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-06-07 10:03:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:03:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.005 |  |
| 2026-06-07 10:03:44 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-06-07 10:03:35 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:03:27 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 10:03:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-07 10:02:37 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-07 10:02:31 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:22 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 10:02:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:19 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:09 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.183 |  |
| 2026-06-07 10:01:20 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.924 |  |
| 2026-06-07 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.121 |  |
| 2026-06-07 10:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:00:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 10:06:44 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-06-07 09:05:06 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-06-07 10:07:01 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-07 10:11:08 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-07 10:03:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-07 10:06:23 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-07 10:02:37 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-07 10:05:35 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-07 10:05:27 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-07 10:10:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-07 10:05:05 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-07 10:06:36 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 10:19:30 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 10:03:27 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 10:02:22 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 10:10:57 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 10:02:31 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:09:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:05:52 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:03:35 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:02:19 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:03:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:07:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:04:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 10:03:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.005 |  |
| 2026-06-07 10:07:23 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-07 10:04:18 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-07 10:04:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-06-07 10:00:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-06-07 10:03:44 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-06-07 10:05:16 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.030 |  |
| 2026-06-07 10:05:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-06-07 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.121 |  |
| 2026-06-07 10:02:09 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.183 |  |
| 2026-06-07 10:01:20 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.924 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)