# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_18:11:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 18:11:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 18:08:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-21 18:08:09 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.046 |  |
| 2026-06-21 18:07:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:26 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-21 18:07:25 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:00 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:06:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:06:08 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-21 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:03:48 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:03:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:03:36 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 18:03:33 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-21 18:03:11 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 18:02:51 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-21 18:02:51 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-06-21 18:02:50 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-21 18:02:39 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:02:29 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:02:19 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:02:19 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:02:08 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 18:01:51 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-21 18:01:51 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:50 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:34 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 18:01:20 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:10 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.034 |  |
| 2026-06-21 18:00:46 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.012 |  |
| 2026-06-21 18:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:00:22 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 18:00:21 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-21 18:00:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 18:03:33 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-21 18:08:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-21 18:06:08 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-21 18:02:51 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 18:07:26 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-21 18:01:51 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-21 18:02:50 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-21 18:03:36 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 18:00:21 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-21 18:00:22 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 18:03:11 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 18:11:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 18:02:08 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:06:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:20 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:03:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:02:19 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:00:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:25 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:00 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:34 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:01:50 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:02:29 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:02:19 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:51 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:00:46 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.012 |  |
| 2026-06-21 18:03:48 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:02:39 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 18:01:10 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.034 |  |
| 2026-06-21 18:02:51 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-06-21 18:08:09 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)