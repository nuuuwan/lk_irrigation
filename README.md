# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_10:35:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 10:35:24 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-14 10:18:58 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.016 |  |
| 2026-03-14 10:14:28 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:11:32 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-14 10:08:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:08:32 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:07:16 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:07:08 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-03-14 10:06:36 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-03-14 10:06:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.078 |  |
| 2026-03-14 10:05:07 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:04:07 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.297 |  |
| 2026-03-14 10:03:58 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-03-14 10:03:50 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-14 10:03:47 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.561 | 🔺 Rising |
| 2026-03-14 10:03:23 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:03:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:03:19 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.089 |  |
| 2026-03-14 10:03:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-03-14 10:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-03-14 10:02:49 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.081 |  |
| 2026-03-14 10:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-14 10:02:31 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-14 10:02:12 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 10:02:09 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-14 10:02:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:02:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:57 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2026-03-14 10:01:49 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 10:01:43 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 10:01:36 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 10:01:26 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:07 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:07 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:00:41 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:00:19 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:00:16 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 10:03:47 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.561 | 🔺 Rising |
| 2026-03-14 10:02:12 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 10:02:09 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-14 10:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-14 10:01:36 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 10:01:49 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 10:01:43 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 10:35:24 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-14 10:00:19 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:02:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:07 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:00:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:07:16 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:03:23 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:14:28 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:26 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:03:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:00:16 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:02:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:08:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:06:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:05:07 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:08:32 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:01:07 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:00:41 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 10:11:32 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-14 10:03:50 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-14 10:02:31 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-14 10:01:57 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2026-03-14 10:18:58 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.016 |  |
| 2026-03-14 10:07:08 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-03-14 10:06:36 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-03-14 10:03:58 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-03-14 10:03:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-03-14 10:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-03-14 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.078 |  |
| 2026-03-14 10:02:49 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.081 |  |
| 2026-03-14 10:03:19 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.089 |  |
| 2026-03-14 10:04:07 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.297 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)