# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_20:16:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 20:16:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.017 |  |
| 2026-02-02 20:16:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:12:48 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 20:11:58 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:11:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-02 20:08:31 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 20:08:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-02-02 20:08:07 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 20:07:38 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:06:00 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:05:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-02-02 20:05:26 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 20:05:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:05:04 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:04:24 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-02 20:03:59 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:03:39 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 20:03:38 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:03:32 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-02-02 20:03:29 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.066 |  |
| 2026-02-02 20:03:15 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-02-02 20:03:01 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.024 |  |
| 2026-02-02 20:02:49 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:02:48 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:02:34 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-02 20:02:25 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:02:23 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:02:18 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:01:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-02 20:01:45 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-02-02 20:01:38 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 20:02:34 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-02 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-02 20:01:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-02 20:04:24 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-02 20:12:48 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 20:08:07 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 20:08:31 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 20:03:39 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 20:01:17 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 20:02:48 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:03:59 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:00:41 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:01:38 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:05:04 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:11:58 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:03:38 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:05:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:07:38 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:02:25 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:16:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:02:23 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:00:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-02 20:08:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-02-02 20:05:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-02-02 20:02:18 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:02:49 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:06:00 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-02-02 20:16:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.017 |  |
| 2026-02-02 20:03:15 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-02-02 20:01:45 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-02-02 20:05:26 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 20:03:32 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-02-02 20:03:01 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.024 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-02 20:03:29 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)