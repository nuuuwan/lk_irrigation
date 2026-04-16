# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_06:33:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 06:33:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.001 |  |
| 2026-04-16 06:20:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-04-16 06:12:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-16 06:10:52 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:08:39 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-16 06:08:38 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-16 06:08:31 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-04-16 06:07:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:07:32 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-16 06:06:08 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-04-16 06:05:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-16 06:05:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-16 06:05:11 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:05:07 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.011 |  |
| 2026-04-16 06:04:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:04:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:04:03 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.076 |  |
| 2026-04-16 06:04:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:03:29 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-16 06:03:20 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.041 |  |
| 2026-04-16 06:03:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-04-16 06:03:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:02:48 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-04-16 06:02:44 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:02:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-16 06:02:17 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-16 06:02:05 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-16 06:02:00 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.031 |  |
| 2026-04-16 06:01:58 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-16 06:01:58 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.898 |  |
| 2026-04-16 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-16 06:01:53 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-04-16 06:01:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:01:41 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.060 |  |
| 2026-04-16 06:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-16 06:00:26 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:00:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-04-16 05:45:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 06:08:39 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-16 05:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-16 06:02:48 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-04-16 05:04:06 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-16 06:12:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-16 06:02:05 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-16 06:07:32 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-16 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-16 06:01:58 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-16 06:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-16 06:05:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-16 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-16 06:04:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:10:52 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:01:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:03:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:02:44 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:04:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:07:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:02:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:05:11 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:04:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 06:33:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.001 |  |
| 2026-04-16 06:08:31 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-04-16 06:05:07 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.011 |  |
| 2026-04-16 06:05:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-16 06:03:29 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-16 06:01:53 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-04-16 06:03:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-04-16 06:00:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-04-16 06:02:00 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.031 |  |
| 2026-04-16 06:03:20 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.041 |  |
| 2026-04-16 06:20:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-04-16 06:06:08 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-04-16 06:01:41 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.060 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 06:02:17 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-04-16 06:04:03 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.076 |  |
| 2026-04-16 06:01:58 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.898 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)