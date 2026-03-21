# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_13:15:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 13:15:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:13:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-03-21 13:12:11 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-03-21 13:12:02 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:10:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-21 13:07:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-21 13:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-03-21 13:06:59 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.064 |  |
| 2026-03-21 13:06:17 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-03-21 13:05:46 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:05:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-21 13:05:02 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:04:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:04:12 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:04:02 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:57 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:28 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:24 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:59 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:02:48 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:39 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:25 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 13:02:16 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.073 |  |
| 2026-03-21 13:02:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-03-21 13:01:18 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:14 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:13 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:01:08 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:08 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:00:59 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:00:53 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.152 |  |
| 2026-03-21 13:00:48 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:00:41 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-21 13:00:13 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 13:07:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-21 13:10:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-21 13:05:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-21 13:02:25 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 13:04:12 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:57 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:14 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:39 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:00:13 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:00:48 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:48 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:04:02 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:28 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:12:02 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:05:02 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:00:59 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:03:24 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:15:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:08 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:01:18 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-03-21 13:05:46 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:04:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:02:59 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:01:08 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:01:13 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:06:17 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-03-21 13:13:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-03-21 13:00:41 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-21 13:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-03-21 13:12:11 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-03-21 13:06:59 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.064 |  |
| 2026-03-21 13:02:16 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.073 |  |
| 2026-03-21 13:00:53 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)