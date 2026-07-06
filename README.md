# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_06:33:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,584 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 06:33:03 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.003 |  |
| 2026-07-06 06:17:19 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-06 06:08:28 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-07-06 06:07:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-07-06 06:07:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:07:09 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:06:47 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:06:45 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.148 |  |
| 2026-07-06 06:06:32 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:06:17 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:05:34 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 06:05:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:05:15 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:05:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-06 06:05:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 06:04:55 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.015 |  |
| 2026-07-06 06:03:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-07-06 06:03:43 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.045 |  |
| 2026-07-06 06:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-07-06 06:02:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-07-06 06:02:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:36 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:02:34 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:31 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-07-06 06:02:26 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 06:02:17 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.052 |  |
| 2026-07-06 06:02:01 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-07-06 06:02:00 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:01:43 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:00:58 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 06:00:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.014 |  |
| 2026-07-06 06:00:44 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:00:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:55:45 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:50:03 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 06:07:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-07-06 06:00:58 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 06:05:34 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 06:05:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 06:05:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-06 06:02:26 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 05:00:58 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 06:17:19 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-06 06:33:03 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.003 |  |
| 2026-07-06 06:02:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:00:44 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:06:32 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:34 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:01:43 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:06:17 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:05:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:07:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:07:09 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-06 05:55:45 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:05:15 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:02:00 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 06:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:02:36 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-06 05:01:20 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:00:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-06 06:00:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.014 |  |
| 2026-07-06 06:04:55 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.015 |  |
| 2026-07-06 06:03:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-07-06 06:02:01 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-07-06 06:02:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-07-06 06:02:31 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-07-06 06:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-07-06 06:08:28 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-07-06 06:03:43 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.045 |  |
| 2026-07-06 06:02:17 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.052 |  |
| 2026-07-06 06:06:45 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)