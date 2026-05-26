# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_10:15:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 10:15:29 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:14:43 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-05-26 10:12:42 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:11:07 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.033 |  |
| 2026-05-26 10:11:00 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-05-26 10:09:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:09:47 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.084 |  |
| 2026-05-26 10:09:34 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-05-26 10:08:22 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-05-26 10:08:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 10:07:55 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:07:31 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-26 10:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-26 10:06:10 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-26 10:06:09 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 10:05:48 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:05:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:04:37 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-05-26 10:04:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:04:33 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 10:04:27 | Glencourse (Kelani Ganga) | 12.64 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-26 10:04:24 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.039 |  |
| 2026-05-26 10:04:24 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:03:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:03:47 | Hanwella (Kelani Ganga) | 4.34 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-26 10:03:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 10.517 | 🔺 Rising |
| 2026-05-26 10:03:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-26 10:03:05 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-05-26 10:02:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:02:28 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.081 |  |
| 2026-05-26 10:02:18 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 10.517 | 🔺 Rising |
| 2026-05-26 10:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-05-26 10:02:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:58 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:39 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:28 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:25 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:00:49 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:00:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 10:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-26 10:03:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 10.517 | 🔺 Rising |
| 2026-05-26 10:11:00 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-05-26 10:03:47 | Hanwella (Kelani Ganga) | 4.34 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-26 10:04:27 | Glencourse (Kelani Ganga) | 12.64 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-26 10:06:10 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-26 10:03:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-26 10:04:33 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 10:06:09 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 10:03:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:04:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:05:48 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 10:08:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 10:01:39 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:05:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:00:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:58 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:02:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:09:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-26 09:06:24 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:28 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:00:49 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:07:55 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:01:25 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:12:42 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:15:29 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:02:28 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:04:24 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:14:43 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.008 |  |
| 2026-05-26 10:04:37 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-05-26 10:07:31 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-26 10:09:34 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-05-26 10:08:22 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-05-26 10:03:05 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-05-26 10:11:07 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.033 |  |
| 2026-05-26 10:04:24 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.039 |  |
| 2026-05-26 10:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-05-26 10:02:28 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.081 |  |
| 2026-05-26 10:09:47 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)