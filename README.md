# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_23:10:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 23:10:28 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.306 |  |
| 2026-06-03 23:10:00 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-06-03 23:08:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-03 23:08:20 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:07:29 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:07:24 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:06:29 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:06:07 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-03 23:06:05 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 23:06:04 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 23:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 23:04:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:04:11 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-03 23:04:05 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:39 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-03 23:03:38 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:32 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:02 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:02:39 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 23:02:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:02:29 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 23:02:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-03 23:01:51 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:01:31 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-03 23:01:18 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-03 23:01:17 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:00:53 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:00:37 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-03 22:58:10 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-03 22:48:55 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.306 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 23:04:11 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-06-03 23:06:07 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-03 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-03 23:00:37 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-03 23:01:18 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-03 23:02:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-03 23:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 23:02:29 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 23:02:39 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 23:06:04 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 23:06:05 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 23:07:29 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:07:24 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:38 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:01:31 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:02 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:01:17 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 22:06:28 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:01:51 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-06-03 22:03:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:41 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:32 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:02:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:20 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 22:03:43 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:04:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:06:29 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:04:05 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-03 22:00:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-03 23:10:00 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-06-03 23:03:39 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-03 22:05:47 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.033 |  |
| 2026-06-03 23:10:28 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.306 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)