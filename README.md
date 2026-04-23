# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_11:09:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 11:09:36 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:08:31 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | -0.119 |  |
| 2026-04-23 11:08:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-04-23 11:07:07 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.035 |  |
| 2026-04-23 11:06:57 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:06:47 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:06:41 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-04-23 11:06:39 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.036 |  |
| 2026-04-23 11:06:31 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.080 |  |
| 2026-04-23 11:06:28 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 11:05:56 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-04-23 11:05:20 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:05:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:05:12 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-04-23 11:04:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:04:08 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:03:54 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:03:35 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:03:14 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.051 |  |
| 2026-04-23 11:03:11 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 11:03:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-04-23 11:02:45 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.013 |  |
| 2026-04-23 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.022 |  |
| 2026-04-23 11:02:18 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:02:07 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:02:03 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:01:58 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-04-23 11:01:56 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:01:49 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:01:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-23 11:01:26 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-23 11:01:19 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.122 |  |
| 2026-04-23 11:01:15 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.050 |  |
| 2026-04-23 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-04-23 11:00:18 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 11:00:16 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.015 |  |
| 2026-04-23 10:49:47 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.035 |  |
| 2026-04-23 10:33:30 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.036 |  |
| 2026-04-23 10:24:45 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 11:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-23 11:06:28 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-23 11:00:18 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 11:03:11 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 11:01:56 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:09:36 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:05:20 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:20:08 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:03:54 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:03:35 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:02:03 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:05:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:06:57 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:01:49 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:04:08 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:02:18 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 11:06:41 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-04-23 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-04-23 11:02:45 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.013 |  |
| 2026-04-23 11:00:16 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.015 |  |
| 2026-04-23 11:08:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-04-23 11:05:12 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-04-23 11:04:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:06:47 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:01:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-23 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.022 |  |
| 2026-04-23 11:03:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-04-23 11:01:58 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-04-23 11:01:26 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-04-23 11:07:07 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.035 |  |
| 2026-04-23 11:06:39 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.036 |  |
| 2026-04-23 11:05:56 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-04-23 11:01:15 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.050 |  |
| 2026-04-23 11:03:14 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.051 |  |
| 2026-04-23 11:06:31 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.080 |  |
| 2026-04-23 10:20:08 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.102 |  |
| 2026-04-23 11:08:31 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | -0.119 |  |
| 2026-04-23 11:01:19 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)