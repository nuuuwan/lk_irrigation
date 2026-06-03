# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_21:11:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 21:11:46 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:11:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.060 |  |
| 2026-06-03 21:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 21:08:44 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 21:08:05 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 21:05:58 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 21:05:49 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-03 21:05:46 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:05:11 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-03 21:05:11 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-06-03 21:04:52 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:04:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 21:04:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2026-06-03 21:04:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:04:01 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-06-03 21:04:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-03 21:04:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-03 21:03:48 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.120 |  |
| 2026-06-03 21:03:28 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:18 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:09 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 21:03:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:52 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:49 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:31 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 21:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:01:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-06-03 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-03 21:00:30 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:00:26 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-06-03 21:00:14 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 21:03:09 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-03 21:05:49 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-03 21:05:11 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-03 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-03 21:08:05 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 21:03:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 21:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 21:02:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-03 21:05:58 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 21:04:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 21:08:44 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 21:04:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:00:14 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:31 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:48 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:00:30 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:04:52 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:49 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:04:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:02:52 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:28 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:03:18 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:11:46 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:05:46 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 21:04:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-03 21:04:01 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-06-03 21:00:26 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-06-03 21:01:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-06-03 21:05:11 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-06-03 20:10:32 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.049 |  |
| 2026-06-03 21:11:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.060 |  |
| 2026-06-03 21:04:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2026-06-03 21:03:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)