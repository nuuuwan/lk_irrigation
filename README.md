# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_05:19:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,945 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 05:19:56 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-03-13 05:19:54 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-03-13 05:16:38 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-13 05:12:06 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:11:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:09:52 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-13 05:09:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:09:17 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 05:08:09 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-03-13 05:07:51 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-13 05:07:24 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.027 |  |
| 2026-03-13 05:05:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:04:58 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-13 05:04:45 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-03-13 05:04:34 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:04:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-13 05:04:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:04:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 05:03:51 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.135 |  |
| 2026-03-13 05:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-13 05:03:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-13 05:03:25 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:03:12 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-13 05:02:48 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-13 05:02:23 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:16 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:14 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 05:01:59 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:01:56 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-13 05:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:01:47 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.053 |  |
| 2026-03-13 05:01:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:01:08 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:00:42 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:00:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 05:19:56 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-03-13 05:04:58 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-13 05:09:17 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-13 04:03:57 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-13 05:09:52 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-13 05:07:51 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-13 05:04:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 05:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-13 05:02:14 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 05:01:08 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:00:42 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:04:34 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:12:06 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:23:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:01:59 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:11:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:00:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:09:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:48 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:05:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:16 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:04:22 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:02:23 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 05:16:38 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-13 05:03:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-13 05:03:12 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-13 05:01:56 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-13 05:04:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-13 05:07:24 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.027 |  |
| 2026-03-13 05:08:09 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-03-13 05:04:45 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.048 |  |
| 2026-03-13 05:01:47 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.053 |  |
| 2026-03-13 05:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-13 05:03:51 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)