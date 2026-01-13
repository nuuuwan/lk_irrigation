# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_08:28:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 08:28:30 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-01-13 08:13:10 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-01-13 08:10:47 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-13 08:10:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 08:09:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:09:13 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:07:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:07:19 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:07:07 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-13 08:06:23 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.037 |  |
| 2026-01-13 08:06:07 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-01-13 08:05:39 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.048 |  |
| 2026-01-13 08:05:37 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:05:33 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-13 08:03:48 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.057 |  |
| 2026-01-13 08:03:47 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-13 08:03:39 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-01-13 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:03:06 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 08:02:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 08:02:50 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:02:37 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:32 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 08:02:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:14 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:02:10 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:09 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-01-13 08:02:00 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:00 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 08:01:53 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:01:50 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 08:01:05 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:00:49 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-01-13 08:00:42 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 08:00:37 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 08:05:33 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-13 08:03:47 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-13 08:02:32 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 08:03:06 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 08:02:00 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 08:10:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 08:02:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 08:00:42 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 08:02:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:00 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:07:19 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 07:22:42 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:37 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:05:37 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:01:53 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:00:37 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:02:10 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:07:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:09:13 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:09:59 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:28:30 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-01-13 08:10:47 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-13 08:03:39 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 08:01:50 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 08:00:49 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-01-13 08:13:10 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-01-13 08:02:14 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:01:05 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:02:50 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-01-13 08:07:07 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-01-13 08:06:23 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.037 |  |
| 2026-01-13 08:06:07 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-01-13 08:02:09 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-01-13 08:05:39 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.048 |  |
| 2026-01-13 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-01-13 08:03:48 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)