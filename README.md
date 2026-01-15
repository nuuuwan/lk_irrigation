# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_06:32:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,988 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 06:32:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-01-15 06:24:32 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.854 | 🔺 Rising |
| 2026-01-15 06:12:52 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:11:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.026 |  |
| 2026-01-15 06:10:50 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:09:11 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:08:17 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-15 06:07:37 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-01-15 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 06:07:26 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.057 |  |
| 2026-01-15 06:07:19 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:07:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:06:38 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.048 |  |
| 2026-01-15 06:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.026 |  |
| 2026-01-15 06:06:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -1.286 |  |
| 2026-01-15 06:05:50 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -1.286 |  |
| 2026-01-15 06:05:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-01-15 06:04:43 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-15 06:04:10 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-15 06:03:52 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.060 |  |
| 2026-01-15 06:03:38 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-01-15 06:03:33 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-01-15 06:03:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:16 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:55 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:20 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:14 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-01-15 06:01:54 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:38 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:27 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:19 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-15 06:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:10 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.044 |  |
| 2026-01-15 06:01:10 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-15 06:00:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 06:00:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:00:09 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.206 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 06:24:32 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.854 | 🔺 Rising |
| 2026-01-15 06:04:43 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-01-15 06:00:47 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 06:01:10 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-15 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 06:04:10 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-15 06:03:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:38 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:12:52 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:55 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:16 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:20 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:54 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:09:11 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:02:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:00:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:10:50 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:07:19 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:03:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:32:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-01-15 06:08:17 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-15 06:03:38 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-01-15 06:07:37 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-01-15 06:03:33 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 06:02:14 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-01-15 06:11:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.026 |  |
| 2026-01-15 06:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.026 |  |
| 2026-01-15 06:01:10 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.044 |  |
| 2026-01-15 06:06:38 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.048 |  |
| 2026-01-15 06:01:19 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-15 06:05:39 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-01-15 06:07:26 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.057 |  |
| 2026-01-15 06:03:52 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.060 |  |
| 2026-01-15 06:00:09 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.206 |  |
| 2026-01-15 06:06:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -1.286 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)