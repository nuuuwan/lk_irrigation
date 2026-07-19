# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_05:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 05:03:22 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.177 |  |
| 2026-07-20 05:02:50 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-07-20 05:02:41 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-20 05:02:14 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-20 05:02:11 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-20 05:01:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:34 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:22 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | 1.827 | 🔺 Rising |
| 2026-07-20 05:01:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-20 05:01:03 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 05:00:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 05:00:10 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:36:08 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:25:51 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-20 04:24:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:16:56 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 05:01:22 | Pitabeddara (Nilwala Ganga) | 2.00 | 🟢 Normal | 1.827 | 🔺 Rising |
| 2026-07-20 04:07:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-07-20 04:04:23 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-07-20 04:08:02 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-20 04:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-20 05:02:14 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-20 05:02:01 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-20 05:01:03 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 04:00:36 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 05:00:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:07:34 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 04:02:34 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 23:01:42 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:34 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:11:34 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:04:39 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-19 21:20:26 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:36:08 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:24:56 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 03:00:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:00:10 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:03:02 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:02:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 18:02:15 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:05:07 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:01:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 05:02:11 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 04:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-07-20 05:01:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-20 05:02:41 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:02:25 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-20 04:16:56 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-07-19 18:03:00 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.019 |  |
| 2026-07-20 05:02:50 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-07-20 05:03:22 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.177 |  |
| 2026-07-20 04:08:28 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -48.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)