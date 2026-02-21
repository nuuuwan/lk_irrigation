# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_17:53:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,250 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 17:53:34 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 17:43:11 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:42:52 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:17:51 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-21 17:16:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:14:21 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-02-21 17:11:51 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-21 17:10:55 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-02-21 17:09:20 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-21 17:08:54 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:07:23 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-21 17:06:59 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 17:06:28 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 17:06:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 17:05:53 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:05:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 17:05:18 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-02-21 17:05:05 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:04:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:04:13 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 17:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:36 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:03:35 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:03:32 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-21 17:03:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.059 |  |
| 2026-02-21 17:03:02 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:03:02 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:02:55 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:02:47 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 17:02:42 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-21 17:02:29 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 17:01:51 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:01:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-21 17:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-21 17:01:33 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.094 |  |
| 2026-02-21 17:01:03 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-02-21 17:01:02 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:00:44 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-21 17:00:19 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 17:00:10 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 17:10:55 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-02-21 17:00:44 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-02-21 17:05:18 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-02-21 17:01:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-21 17:07:23 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-21 17:03:32 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-21 17:02:42 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-21 17:09:20 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-21 17:04:13 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-21 17:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-21 17:11:51 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-21 17:17:51 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-21 17:53:34 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 17:06:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 17:02:47 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 17:05:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 17:06:59 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 17:02:29 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 17:06:28 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 17:04:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:43:11 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:01:33 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:05:53 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:02 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:16:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:05:05 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:08:54 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:02:55 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:01:02 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 17:03:35 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:03:02 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:03:36 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-21 17:00:10 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-02-21 17:14:21 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-02-21 17:01:03 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-02-21 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.059 |  |
| 2026-02-21 17:01:26 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)