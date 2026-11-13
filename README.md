# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_05:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,280 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 05:02:48 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:02:39 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:19 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.062 |  |
| 2026-11-14 05:02:18 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:11 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | -0.021 |  |
| 2026-11-14 05:02:09 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-11-14 05:01:38 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:00:18 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:00:09 | Weraganthota (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-11-14 04:31:08 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 03:18:05 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 05:02:11 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | -0.021 |  |
| 2026-11-14 04:13:43 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.030 |  |
| 2026-11-14 04:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | -0.040 |  |
| 2026-11-14 05:00:09 | Weraganthota (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-11-14 04:02:43 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-14 04:06:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-14 05:00:18 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:39 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:02:12 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:03:37 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 05:02:18 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:03:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:10:50 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:03:06 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:14:03 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-14 04:31:08 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.007 |  |
| 2026-11-14 04:04:44 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-14 04:02:39 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-14 04:04:00 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-14 04:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-14 04:01:59 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-11-14 04:02:48 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-14 04:03:10 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-11-14 04:02:04 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:02:48 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 05:01:38 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 04:00:15 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.021 |  |
| 2026-11-14 04:02:07 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.021 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 04:05:04 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-11-14 04:03:05 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-14 03:01:34 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-11-14 04:11:08 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.050 |  |
| 2026-11-14 05:02:19 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.062 |  |
| 2026-11-14 05:02:09 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-11-14 03:18:52 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -90.000 |  |
| 2026-11-14 03:11:43 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)