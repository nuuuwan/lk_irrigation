# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_07:02:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,101 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 07:02:41 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:02:30 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 07:02:17 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-20 07:02:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:48 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:45 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 07:01:13 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 06:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.791 | 🔺 Rising |
| 2026-07-20 06:08:44 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-20 06:00:58 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-20 07:02:17 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-20 06:04:05 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-20 07:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 06:00:43 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-20 06:03:58 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-20 07:01:45 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 07:02:30 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 23:01:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:48 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:04:59 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:02:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:39 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 21:20:26 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:10:18 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:02:41 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:06:09 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:04:26 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:17:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:08:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:03:35 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:03:33 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:04:04 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:08:43 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:00:19 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:08:35 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 07:01:13 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-20 06:01:46 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.011 |  |
| 2026-07-20 06:01:29 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.011 |  |
| 2026-07-20 06:05:35 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-07-20 06:10:04 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.037 |  |
| 2026-07-20 06:07:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.042 |  |
| 2026-07-20 06:04:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.127 |  |
| 2026-07-20 06:05:41 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.221 |  |
| 2026-07-20 06:00:09 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -1.715 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)