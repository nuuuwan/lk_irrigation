# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_05:10:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 05:10:40 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-06-06 05:09:15 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.076 |  |
| 2026-06-06 05:07:58 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-06 05:07:44 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.061 |  |
| 2026-06-06 05:06:41 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.087 |  |
| 2026-06-06 05:06:26 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-06 05:06:24 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-06 05:05:42 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-06 05:05:04 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 05:04:34 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:04:16 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:04:05 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 05:04:03 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-06-06 05:03:23 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.051 |  |
| 2026-06-06 05:03:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:03:15 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.037 |  |
| 2026-06-06 05:03:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-06-06 05:02:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:02:55 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:02:46 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.196 |  |
| 2026-06-06 05:02:45 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.000 |  |
| 2026-06-06 05:02:26 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 05:02:10 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 05:02:06 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-06 05:01:39 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:01:26 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:00:26 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-06-06 04:54:10 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-06 04:50:30 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.196 |  |
| 2026-06-06 04:37:47 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.076 |  |
| 2026-06-06 04:22:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 05:02:45 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | 0.000 |  |
| 2026-06-06 05:05:42 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-06 04:54:10 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-06 05:04:05 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 04:02:49 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 05:02:10 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 05:02:26 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 04:22:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-06 05:02:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:02:55 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:01:26 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:03:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:02:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:01:39 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:04:03 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:04:34 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:15:25 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:16:55 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:04:16 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 04:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 05:06:24 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-06 05:06:26 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-06 05:05:04 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 05:10:40 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-06 05:00:26 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-06-06 05:02:06 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-06 05:07:58 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-06 04:03:30 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.027 |  |
| 2026-06-06 05:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-06-06 05:03:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-06-06 05:03:15 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.037 |  |
| 2026-06-06 05:03:23 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.051 |  |
| 2026-06-06 05:07:44 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.061 |  |
| 2026-06-06 05:09:15 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.076 |  |
| 2026-06-06 05:06:41 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.087 |  |
| 2026-06-06 05:02:46 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)