# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_11:26:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 11:26:43 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.014 |  |
| 2026-03-15 11:20:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-03-15 11:15:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:10:59 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.026 |  |
| 2026-03-15 11:10:12 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.063 |  |
| 2026-03-15 11:09:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-03-15 11:07:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:07:02 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-03-15 11:06:49 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 11:06:09 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:05:44 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:05:32 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-03-15 11:04:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:04:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.076 |  |
| 2026-03-15 11:04:01 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-15 11:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-03-15 11:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:03:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-03-15 11:03:23 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-15 11:03:16 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:03:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:03:09 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.032 |  |
| 2026-03-15 11:03:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-03-15 11:02:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-03-15 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-15 11:02:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:02:26 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-03-15 11:02:00 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 11:01:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:32 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:13 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-15 11:01:08 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:04 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:00:55 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:00:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-15 11:00:36 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 11:03:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-03-15 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-15 11:02:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-03-15 10:01:37 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-15 11:06:49 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 11:02:00 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 11:01:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:04 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:02:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:32 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:07:26 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:03:16 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:00:36 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:05:44 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:04:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:00:55 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:15:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:01:08 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 11:20:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-03-15 11:07:02 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-03-15 11:03:33 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:00:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:06:09 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:03:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-15 11:03:23 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-15 11:09:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-03-15 11:26:43 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.014 |  |
| 2026-03-15 11:04:01 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-15 11:03:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-03-15 11:10:59 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.026 |  |
| 2026-03-15 11:05:32 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-03-15 11:01:13 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-15 11:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-03-15 11:03:09 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.032 |  |
| 2026-03-15 11:02:26 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-03-15 11:10:12 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.063 |  |
| 2026-03-15 11:04:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)