# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_04:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 04:12:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.076 |  |
| 2026-05-01 04:10:52 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:09:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-01 04:08:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.113 |  |
| 2026-05-01 04:07:41 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:07:24 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-05-01 04:06:24 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:04:58 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:04:40 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-01 04:03:59 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-05-01 04:03:53 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:03:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-05-01 04:02:48 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-01 04:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-05-01 04:02:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:02:27 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:02:16 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 04:02:10 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-01 04:02:09 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-01 04:01:10 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.129 |  |
| 2026-05-01 04:00:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:00:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-01 04:00:51 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-01 04:00:48 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.041 |  |
| 2026-05-01 03:59:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-05-01 03:32:29 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 04:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 5.625 | 🔺 Rising |
| 2026-05-01 04:07:24 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-05-01 04:02:48 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-01 04:00:51 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-01 04:04:40 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-01 04:02:16 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 04:02:29 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:00:56 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:02:27 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:04:58 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:05:06 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:06:24 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:03:53 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:07:41 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:10:52 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:03:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 04:09:34 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:04:09 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 04:02:09 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 04:03:59 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-05-01 00:03:12 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-01 04:00:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-01 04:02:10 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-01 04:00:48 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.041 |  |
| 2026-05-01 00:05:11 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-05-01 03:06:36 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.053 |  |
| 2026-05-01 04:12:18 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.076 |  |
| 2026-05-01 04:08:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.113 |  |
| 2026-05-01 04:01:10 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.129 |  |
| 2026-05-01 02:06:43 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)