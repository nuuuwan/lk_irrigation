# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_17:13:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,880 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 17:13:38 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.035 |  |
| 2026-06-18 17:10:46 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-06-18 17:10:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:07:56 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-18 17:07:27 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-06-18 17:07:23 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-18 17:07:11 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:06:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:06:45 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 17:05:41 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.021 |  |
| 2026-06-18 17:05:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 17:05:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:05:27 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-06-18 17:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-18 17:04:47 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 17:04:41 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:04:28 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:03:59 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-06-18 17:03:37 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-06-18 17:03:29 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.111 |  |
| 2026-06-18 17:03:04 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 17:03:00 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:02:58 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 17:02:45 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:02:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:02:21 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:46 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:37 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-18 17:01:34 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:29 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:10 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:01:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:00:40 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-18 17:00:21 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:00:20 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 17:00:10 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 17:07:27 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-06-18 17:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-18 17:01:37 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-18 17:07:23 | Glencourse (Kelani Ganga) | 10.52 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-18 17:00:40 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-18 17:06:45 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-18 17:07:56 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-18 17:05:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 17:03:04 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 17:00:20 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 17:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 17:04:47 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 17:05:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:12:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:34 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:02:21 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:46 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:10:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:04:41 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:07 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:04:28 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:06:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:02:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:01:29 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:00:10 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:00:21 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:02:45 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 17:07:11 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:03:00 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:01:10 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:02:58 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-18 17:10:46 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-06-18 17:05:27 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-06-18 17:03:37 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-06-18 17:05:41 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.021 |  |
| 2026-06-18 17:03:59 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-06-18 17:13:38 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.035 |  |
| 2026-06-18 17:03:29 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)