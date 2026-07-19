# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19_18:10:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **210,681 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 18:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.061 |  |
| 2026-07-19 18:10:24 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:09:19 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-19 18:08:07 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:08:04 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-19 18:06:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-07-19 18:06:49 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:06:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-07-19 18:05:43 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:05:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:05:26 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-19 18:05:09 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 18:04:39 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:04 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:36 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:29 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.045 |  |
| 2026-07-19 18:03:15 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:00 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.019 |  |
| 2026-07-19 18:02:54 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.080 |  |
| 2026-07-19 18:02:51 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:50 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:39 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:32 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:03 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:02:01 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:46 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:01:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:13 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:13 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:11 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:00:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:00:09 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 18:05:26 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-19 18:09:19 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-19 18:05:09 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-19 18:08:04 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-19 18:01:11 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:15 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:39 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:10:24 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:08:07 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:51 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:13 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:06:49 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:08 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:01 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:32 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:22 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:39 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:04 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:50 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:05:43 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:03:36 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:01:13 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:05:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:01:46 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:00:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:02:03 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-07-19 18:03:00 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.019 |  |
| 2026-07-19 18:00:09 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.045 |  |
| 2026-07-19 18:03:29 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.045 |  |
| 2026-07-19 18:06:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-07-19 18:06:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-07-19 18:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.061 |  |
| 2026-07-19 18:02:54 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)