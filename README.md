# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_22:19:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 22:19:58 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:14:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.016 |  |
| 2026-07-10 22:13:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:12:58 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:12:17 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-10 22:09:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-10 22:09:00 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-07-10 22:09:00 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:08:34 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:07:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:06:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-10 22:06:17 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:05:41 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-07-10 22:05:06 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 22:05:05 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 22:04:51 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:04:39 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-10 22:04:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:04:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.294 |  |
| 2026-07-10 22:03:56 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:03:36 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:03:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:03:08 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:03:03 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:48 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:40 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:40 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 22:02:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:02:34 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 22:02:23 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-10 22:02:18 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:13 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.063 |  |
| 2026-07-10 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.065 |  |
| 2026-07-10 22:01:49 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:01:26 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:01:10 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 22:09:00 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-07-10 22:12:17 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-10 22:09:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-10 22:02:23 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-10 22:05:06 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 22:05:05 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 22:02:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 22:02:34 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-10 21:15:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-10 22:04:39 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-10 22:03:36 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:02:39 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:03:56 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 22:04:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:40 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:03:08 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:01:49 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:48 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:01:26 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:06:17 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:08:34 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:13:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:12:58 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:18 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:40 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:09:00 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:07:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:19:58 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:02:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:03:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-10 22:05:41 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-07-10 22:06:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-10 22:14:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.016 |  |
| 2026-07-10 22:02:13 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.063 |  |
| 2026-07-10 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.065 |  |
| 2026-07-10 22:04:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.294 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)