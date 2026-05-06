# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_07:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 07:18:49 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:11:17 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:10:07 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.026 |  |
| 2026-05-06 07:09:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.113 |  |
| 2026-05-06 07:09:10 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:08:38 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:08:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:07:48 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-05-06 07:07:28 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-06 07:07:22 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2026-05-06 07:07:01 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:06:51 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-05-06 07:06:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-05-06 07:05:27 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:05:04 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.041 |  |
| 2026-05-06 07:04:54 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-05-06 07:04:45 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:04:28 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 07:04:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:03:47 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 07:03:40 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:03:34 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-06 07:03:14 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-05-06 07:03:14 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 07:02:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:33 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:26 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:26 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.061 |  |
| 2026-05-06 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.078 |  |
| 2026-05-06 07:01:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:01:23 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:00:55 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.002 |  |
| 2026-05-06 07:00:01 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:31:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 07:07:28 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-06 07:04:28 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 07:02:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 07:03:47 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 07:00:55 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.002 |  |
| 2026-05-06 07:00:01 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:09:10 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:01:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:18:49 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:01:23 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:11:17 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:08:38 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:08:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:03:14 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:03:40 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:33 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 07:02:26 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:07:06 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 06:31:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.002 |  |
| 2026-05-06 07:07:48 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-05-06 07:06:51 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-05-06 07:05:27 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:04:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:07:01 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:04:45 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-06 07:06:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-05-06 07:03:34 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-06 07:03:14 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-05-06 07:10:07 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.026 |  |
| 2026-05-06 07:04:54 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-05-06 07:05:04 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.041 |  |
| 2026-05-06 07:02:26 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.061 |  |
| 2026-05-06 06:01:42 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.062 |  |
| 2026-05-06 07:07:22 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2026-05-06 07:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.078 |  |
| 2026-05-06 07:09:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)