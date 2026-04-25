# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_11:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 11:14:47 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:12:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.022 |  |
| 2026-04-25 11:08:46 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.072 |  |
| 2026-04-25 11:08:24 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:08:01 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 32.356 | 🔺 Rising |
| 2026-04-25 11:07:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:38 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-04-25 11:06:22 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-04-25 11:06:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:05 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-04-25 11:06:05 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.067 |  |
| 2026-04-25 11:05:59 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-25 11:05:40 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:05:36 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 11:04:47 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:04:36 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.023 |  |
| 2026-04-25 11:04:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-25 11:04:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:03:54 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 32.356 | 🔺 Rising |
| 2026-04-25 11:03:46 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:03:22 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:03:20 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:03:06 | Katharagama (Menik Ganga) | 1.75 | 🟢 Normal | -0.012 |  |
| 2026-04-25 11:03:05 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-04-25 11:02:55 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-04-25 11:02:11 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:01:43 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:01:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-04-25 11:01:33 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-25 11:01:05 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:00:54 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:00:42 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:00:22 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 11:08:01 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 32.356 | 🔺 Rising |
| 2026-04-25 11:01:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-04-25 11:04:29 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-25 11:05:59 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-25 11:01:33 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-25 11:05:36 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 10:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 11:00:22 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:00:54 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:01:05 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:14:47 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:05:40 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:06:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:07:53 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:03:20 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 11:04:47 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-25 10:08:23 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 11:06:38 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2026-04-25 11:06:22 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-04-25 11:02:11 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:04:03 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:03:46 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-25 11:03:06 | Katharagama (Menik Ganga) | 1.75 | 🟢 Normal | -0.012 |  |
| 2026-04-25 11:01:43 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:08:24 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:03:22 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:00:42 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:02:55 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-25 11:03:05 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-04-25 10:10:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-04-25 11:12:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.022 |  |
| 2026-04-25 11:04:36 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.023 |  |
| 2026-04-25 11:06:05 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-04-25 11:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-04-25 11:06:05 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.067 |  |
| 2026-04-25 11:08:46 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)