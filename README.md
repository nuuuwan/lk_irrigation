# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_09:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 09:05:34 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:04:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:04:42 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.031 |  |
| 2026-02-20 09:04:17 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:52 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 09:03:50 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:49 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-20 09:03:34 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:31 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:21 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:19 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 09:03:18 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.221 |  |
| 2026-02-20 09:03:17 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 09:02:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 09:02:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-02-20 09:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-20 09:01:49 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.022 |  |
| 2026-02-20 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-20 09:01:44 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:36 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-02-20 09:01:26 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:18 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-02-20 09:01:08 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:01 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:00 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:00:50 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-20 08:48:43 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:36:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:31:40 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.041 |  |
| 2026-02-20 08:12:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:11:30 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 08:10:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 08:00:07 | Padiyathalawa (Maduru Oya) | 4.10 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-02-20 09:03:49 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-20 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-20 09:03:52 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-20 08:05:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-20 09:03:19 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 09:00:50 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-20 09:03:17 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 08:02:14 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:05:34 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:25 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:31 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:36:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:44 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:04:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:21 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:50 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:08 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:01 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:03:34 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:24:31 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:26 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:09:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:01:00 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:04:17 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 09:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-20 09:02:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:03:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-02-20 09:01:49 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.022 |  |
| 2026-02-20 09:01:18 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-02-20 09:04:42 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.031 |  |
| 2026-02-20 09:01:36 | Nakkala (Kumbukkan Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-02-20 08:31:40 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.041 |  |
| 2026-02-20 09:02:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-02-20 08:02:47 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.180 |  |
| 2026-02-20 09:03:18 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)