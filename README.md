# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_13:26:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,575 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 13:26:00 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -5.099 |  |
| 2026-04-26 13:20:07 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:17:48 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-04-26 13:16:21 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:09:22 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-26 13:08:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:08:17 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-04-26 13:07:10 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:06:10 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:05:59 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:05:58 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 13:05:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:05:31 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:04:58 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-04-26 13:04:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-26 13:04:49 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.052 |  |
| 2026-04-26 13:03:59 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 13:03:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:03:57 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:03:44 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-26 13:03:29 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:03:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-26 13:02:52 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.048 |  |
| 2026-04-26 13:02:43 | Katharagama (Menik Ganga) | 1.26 | 🟢 Normal | -0.171 |  |
| 2026-04-26 13:02:42 | Urawa (Nilwala Ganga) | 2.00 | 🟢 Normal | -5.099 |  |
| 2026-04-26 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-04-26 13:02:21 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:02:21 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:02:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-26 13:02:18 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.022 |  |
| 2026-04-26 13:02:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:02:10 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-04-26 13:02:05 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-04-26 13:02:04 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:01:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:01:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:00:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:00:39 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 13:04:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-26 13:03:44 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-26 13:03:59 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 13:09:22 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-26 13:05:58 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 13:03:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:00:59 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 12:03:11 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:05:31 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:03:57 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:02:21 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:20:07 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:16:21 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:05:59 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:01:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-26 13:05:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:06:10 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:03:29 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:02:04 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:00:39 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:02:17 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:07:10 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-26 13:02:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-26 13:02:05 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-04-26 13:03:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-26 13:04:58 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-04-26 13:08:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:01:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:02:21 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-04-26 13:02:18 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.022 |  |
| 2026-04-26 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-04-26 13:02:10 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-04-26 13:02:52 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.048 |  |
| 2026-04-26 13:17:48 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-04-26 13:08:17 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-04-26 13:04:49 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.052 |  |
| 2026-04-26 13:02:43 | Katharagama (Menik Ganga) | 1.26 | 🟢 Normal | -0.171 |  |
| 2026-04-26 13:26:00 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -5.099 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)