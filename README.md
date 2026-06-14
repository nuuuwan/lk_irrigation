# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_08:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 08:08:01 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.116 |  |
| 2026-06-14 08:06:53 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:06:32 | Rathnapura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.091 |  |
| 2026-06-14 08:06:29 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-14 08:05:43 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:05:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.020 |  |
| 2026-06-14 08:05:27 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 08:05:24 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.044 |  |
| 2026-06-14 08:05:03 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 08:04:46 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-06-14 08:04:38 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:51 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:49 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.021 |  |
| 2026-06-14 08:03:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:43 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 08:03:23 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:19 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.040 |  |
| 2026-06-14 08:03:06 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:42 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.052 |  |
| 2026-06-14 08:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:02:34 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:02:24 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:02:10 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.051 |  |
| 2026-06-14 08:02:05 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-06-14 08:02:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:01:53 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:01:29 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:01:04 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 08:00:59 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 08:05:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.020 |  |
| 2026-06-14 08:06:29 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-14 08:03:43 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 08:05:03 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 08:00:59 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-14 08:01:04 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 08:05:27 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 08:03:06 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:51 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:03:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:04:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:03:23 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:06:29 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:02:24 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:05:43 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:10:44 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-06-14 08:02:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:04:38 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:01:29 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:02:13 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-14 08:02:34 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:01:53 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:06:53 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:03:49 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.021 |  |
| 2026-06-14 07:03:11 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-06-14 08:04:46 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-06-14 08:02:05 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-06-14 08:03:19 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.040 |  |
| 2026-06-14 07:00:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.040 |  |
| 2026-06-14 08:05:24 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.044 |  |
| 2026-06-14 08:02:10 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.051 |  |
| 2026-06-14 08:02:42 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.052 |  |
| 2026-06-14 08:06:32 | Rathnapura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.091 |  |
| 2026-06-14 08:08:01 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)