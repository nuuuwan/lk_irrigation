# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_06:31:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 06:31:02 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | -0.022 |  |
| 2026-05-14 06:09:05 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | -0.056 |  |
| 2026-05-14 06:08:45 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:07:19 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:06:51 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:06:17 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:06:12 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 06:05:28 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:05:28 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.119 |  |
| 2026-05-14 06:05:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.087 |  |
| 2026-05-14 06:05:08 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.082 |  |
| 2026-05-14 06:04:59 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-14 06:04:54 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:04:09 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-14 06:04:07 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-05-14 06:03:58 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -36.000 |  |
| 2026-05-14 06:03:56 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -36.000 |  |
| 2026-05-14 06:03:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-14 06:03:26 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.059 |  |
| 2026-05-14 06:03:20 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 06:03:15 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:03:09 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.022 |  |
| 2026-05-14 06:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.000 |  |
| 2026-05-14 06:02:30 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.060 |  |
| 2026-05-14 06:02:27 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-14 06:02:25 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.189 |  |
| 2026-05-14 06:02:17 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-14 06:02:10 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-05-14 06:02:02 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-14 06:01:26 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-05-14 06:01:25 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -36.000 |  |
| 2026-05-14 06:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:01:24 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -36.000 |  |
| 2026-05-14 06:01:13 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.179 |  |
| 2026-05-14 06:00:55 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-14 06:00:41 | Rathnapura (Kalu Ganga) | 4.65 | 🟢 Normal | -0.142 |  |
| 2026-05-14 06:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-14 06:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:00:11 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.278 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 06:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.000 |  |
| 2026-05-14 06:01:13 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.179 |  |
| 2026-05-14 06:02:27 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-14 06:04:59 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-14 06:04:09 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-14 06:02:17 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-14 06:06:12 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 05:03:08 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-14 06:03:20 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 06:04:54 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:03:15 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:06:17 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:08:45 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:07:19 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:06:51 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 06:03:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-14 06:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-14 06:02:10 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-05-14 06:04:07 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-05-14 06:00:55 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-05-14 06:31:02 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | -0.022 |  |
| 2026-05-14 06:03:09 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.022 |  |
| 2026-05-14 06:01:26 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 06:09:05 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | -0.056 |  |
| 2026-05-14 06:03:26 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.059 |  |
| 2026-05-14 06:02:02 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-14 06:02:30 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.060 |  |
| 2026-05-14 06:05:08 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.082 |  |
| 2026-05-14 06:05:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.087 |  |
| 2026-05-14 06:05:28 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.119 |  |
| 2026-05-14 06:00:41 | Rathnapura (Kalu Ganga) | 4.65 | 🟢 Normal | -0.142 |  |
| 2026-05-14 06:02:25 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | -0.189 |  |
| 2026-05-14 06:00:11 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.278 |  |
| 2026-05-14 06:03:58 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -36.000 |  |
| 2026-05-14 06:01:25 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)