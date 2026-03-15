# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_10:21:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,923 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 10:21:26 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:19:40 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.008 |  |
| 2026-03-15 10:11:49 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:07:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:07:20 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.046 |  |
| 2026-03-15 10:07:20 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.065 |  |
| 2026-03-15 10:07:17 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-15 10:06:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-03-15 10:06:24 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:06:06 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:29 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:05:04 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-03-15 10:03:48 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.082 |  |
| 2026-03-15 10:03:47 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-03-15 10:03:44 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.020 |  |
| 2026-03-15 10:03:34 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:03:12 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 10:03:04 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.055 |  |
| 2026-03-15 10:02:43 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:02:34 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-03-15 10:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-03-15 10:02:19 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-15 10:02:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:54 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:01:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:37 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-15 10:01:34 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.022 |  |
| 2026-03-15 10:01:11 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-15 10:01:07 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 10:01:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:00:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-03-15 10:00:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:00:32 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | 0.408 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 10:00:32 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-03-15 10:01:11 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-15 10:01:37 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-15 10:01:07 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 10:06:24 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:11:49 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:01:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:06:06 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:07:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:03:15 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:04 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:00:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:02:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:00:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:05:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:21:26 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 10:19:40 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.008 |  |
| 2026-03-15 10:07:17 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-15 10:03:34 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:05:29 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:02:43 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:01:54 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:01:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-15 10:03:12 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 10:03:44 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.020 |  |
| 2026-03-15 10:02:19 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-15 10:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-03-15 10:01:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.022 |  |
| 2026-03-15 10:06:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-03-15 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-03-15 10:07:20 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.046 |  |
| 2026-03-15 10:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.048 |  |
| 2026-03-15 10:03:47 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-03-15 10:03:04 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.055 |  |
| 2026-03-15 10:02:34 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-03-15 10:07:20 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.065 |  |
| 2026-03-15 10:03:48 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)