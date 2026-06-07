# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_20:23:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 20:23:08 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 20:22:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:16:01 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.076 |  |
| 2026-06-07 20:12:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.034 |  |
| 2026-06-07 20:10:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-06-07 20:09:33 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 20:09:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:09:05 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-07 20:08:19 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:07:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:06:41 | Rathnapura (Kalu Ganga) | 4.04 | 🟢 Normal | -0.039 |  |
| 2026-06-07 20:06:40 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 20:06:24 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 20:05:52 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:05:41 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-06-07 20:05:39 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-06-07 20:05:17 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:05:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:05:00 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | -0.062 |  |
| 2026-06-07 20:04:46 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 20:04:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 20:03:57 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 20:03:22 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:03:11 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-06-07 20:03:10 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:39 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:38 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:02:27 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.050 |  |
| 2026-06-07 20:02:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:01:50 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 20:01:39 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-07 20:01:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:01:24 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 20:00:39 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 20:05:41 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-06-07 20:01:39 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-07 20:01:24 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 20:00:39 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-07 20:09:05 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-07 20:04:46 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 20:03:57 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 20:01:50 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 20:09:33 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 20:06:40 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 20:04:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 20:06:24 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 20:23:08 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 20:03:10 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:01:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:08:19 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:09:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:02:39 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:05:17 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:03:22 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:22:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:07:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-06-07 20:10:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-06-07 20:05:52 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:02:38 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:05:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-07 20:03:11 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-06-07 19:02:19 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-06-07 20:05:39 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-06-07 20:12:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.034 |  |
| 2026-06-07 20:06:41 | Rathnapura (Kalu Ganga) | 4.04 | 🟢 Normal | -0.039 |  |
| 2026-06-07 20:02:27 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.050 |  |
| 2026-06-07 20:05:00 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | -0.062 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 20:16:01 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)