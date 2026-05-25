# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_20:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,544 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:22:08 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | -0.023 |  |
| 2026-05-25 20:12:41 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 20:11:21 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:10:47 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.018 |  |
| 2026-05-25 20:10:23 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-05-25 20:07:22 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.077 |  |
| 2026-05-25 20:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:06:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-05-25 20:06:13 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-05-25 20:05:35 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-25 20:05:18 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:05:13 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:05:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:04:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-05-25 20:04:32 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-25 20:04:30 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:03:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.030 |  |
| 2026-05-25 20:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-25 20:03:05 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-25 20:03:00 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:52 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:46 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:42 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:34 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-25 20:02:26 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:18 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:16 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:02:16 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-05-25 20:02:11 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-25 20:01:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:01:34 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | -0.022 |  |
| 2026-05-25 20:01:33 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-25 20:01:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:01:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-25 20:02:11 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-05-25 20:03:05 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-25 20:04:32 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-25 20:05:35 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-25 20:02:34 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-25 20:01:33 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-25 20:12:41 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 20:03:00 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:01:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:01:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:01:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:52 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:04:30 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:26 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:07:13 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:18 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:11:21 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:46 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:02:42 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 20:05:18 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:05:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:02:16 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:05:13 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 20:02:16 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 20:10:23 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-05-25 20:10:47 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.018 |  |
| 2026-05-25 20:06:13 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.019 |  |
| 2026-05-25 20:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 20:01:34 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | -0.022 |  |
| 2026-05-25 20:22:08 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | -0.023 |  |
| 2026-05-25 20:06:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-05-25 20:03:58 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.030 |  |
| 2026-05-25 20:04:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-05-25 20:07:22 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)