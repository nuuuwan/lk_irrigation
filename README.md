# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_05:12:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 05:12:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:10:59 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.075 |  |
| 2026-04-13 05:10:55 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |
| 2026-04-13 05:09:42 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-04-13 05:08:12 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 05:08:02 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-13 05:07:51 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-04-13 05:07:39 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:06:55 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -1.932 |  |
| 2026-04-13 05:06:52 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 05:06:28 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:06:02 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.071 |  |
| 2026-04-13 05:05:50 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-13 05:05:41 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 05:05:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-13 05:05:18 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-13 05:05:04 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 05:04:42 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-13 05:04:34 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.228 |  |
| 2026-04-13 05:04:21 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-13 05:04:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-13 05:03:52 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:03:51 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 05:03:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.025 |  |
| 2026-04-13 05:03:09 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -2.107 |  |
| 2026-04-13 05:02:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:02:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:02:39 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-04-13 05:02:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-04-13 05:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-04-13 05:01:47 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-13 05:01:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-13 05:01:20 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 05:01:09 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:59:44 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -2.107 |  |
| 2026-04-13 04:39:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.025 |  |
| 2026-04-13 04:39:00 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.025 |  |
| 2026-04-13 04:31:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 04:26:49 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-13 04:23:50 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.071 |  |
| 2026-04-13 04:23:48 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 04:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 9.290 | 🔺 Rising |
| 2026-04-13 05:01:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-13 05:05:18 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-13 05:04:42 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-13 05:04:21 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-13 05:05:50 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-13 05:06:52 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-13 05:01:20 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 05:08:12 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 05:03:51 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 05:05:41 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 05:05:04 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 04:02:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:12:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:03:52 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:01:09 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:06:28 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:02:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:02:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:07:39 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 05:05:24 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-13 05:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-04-13 05:08:02 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-13 05:07:51 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-04-13 05:09:42 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-04-13 05:04:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-04-13 05:03:27 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.025 |  |
| 2026-04-13 05:01:47 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-13 05:10:55 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |
| 2026-04-13 05:02:39 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-04-13 05:06:02 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.071 |  |
| 2026-04-13 05:02:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-04-13 05:10:59 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.075 |  |
| 2026-04-13 05:04:34 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.228 |  |
| 2026-04-13 05:06:55 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -1.932 |  |
| 2026-04-13 05:03:09 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -2.107 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)