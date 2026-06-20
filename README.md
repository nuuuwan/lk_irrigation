# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_13:18:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 13:18:29 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:14:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-20 13:12:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:12:46 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 13:09:03 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:08:51 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:08:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-20 13:08:34 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:08:10 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:06:59 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.101 |  |
| 2026-06-20 13:06:59 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-20 13:05:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:05:56 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.066 |  |
| 2026-06-20 13:05:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:05:38 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 13:05:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-20 13:04:37 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:04:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:03:50 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:03:36 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-06-20 13:02:59 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-06-20 13:02:38 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.030 |  |
| 2026-06-20 13:02:27 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:02:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.070 |  |
| 2026-06-20 13:02:15 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-20 13:02:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:02:02 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:02:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:51 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 13:01:10 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:00:57 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:00:46 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 13:00:36 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 13:01:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 13:00:46 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 13:14:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-20 13:05:38 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 13:02:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 13:06:59 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-20 13:12:46 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 13:08:10 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:00:36 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:02:02 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:02:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:12:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:02:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:51 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:05:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:04:37 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:01:10 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:00:57 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 13:18:29 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:05:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:09:03 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-06-20 13:04:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:02:27 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-20 13:02:15 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-06-20 12:08:11 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-06-20 13:03:36 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-06-20 13:08:34 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:03:50 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:08:51 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.019 |  |
| 2026-06-20 13:05:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-20 13:08:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-06-20 13:02:38 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.030 |  |
| 2026-06-20 13:02:59 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.042 |  |
| 2026-06-20 13:05:56 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.066 |  |
| 2026-06-20 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.070 |  |
| 2026-06-20 13:06:59 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)